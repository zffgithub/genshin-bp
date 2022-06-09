const draft = new Vue({
  el: "#app",
  delimiters: ["[[", "]]"],
  data: {
    timer: 0,
    timerF: null,
    start: false,
    laneBlue: false,
    laneRed: false,
    order: 0,
    draft: {
      banpick: "",
      temp: "",
      team: "blue",
    },
    championsList: "",
    championsValid: [],
  },
  watch: {
    timer: function (newTimer, oldTimer) {
      if (master == roomId) {
        if (this.start && newTimer == 31) {
          const self = this;
          if ([0, 1, 2, 3, 8, 9, 10, 11].includes(self.order)) {
            self.draft.temp = "999";
          } else {
            self.draft.temp = randomArray(self.championsValid);
            // if (self.draft.temp) {
            // } else {
            //   self.draft.temp = randomArray(self.championsValid);
            // }
          }
          self.draftChoice();
        }
      }
    },
    order: function (newOrder, oldOrder) {
      const blue = [0, 2, 8, 10, 4, 6, 13, 15];
      if (blue.includes(newOrder)) {
        this.draft.team = "blue";
      } else {
        this.draft.team = "red";
      }
    },
  },
  filters: {
    timerDp(timer) {
      return timer / 30 < 1 ? 29 - (timer % 30) : 0;
    },
    selectClassName(order) {
      return [0, 1, 2, 3, 8, 9, 10, 11].includes(order)
        ? "ban"
        : "pick";
    },
    selectHtml(order) {
      return [0, 1, 2, 3, 8, 9, 10, 11].includes(order)
        ? "禁用"
        : "选择";
    },
    cpClassName(no) {
      return "sp-" + no;
    },
    cpStyle(no) {
      return "backgroundPosition:0px -" + String(Number(no) * 81) + "px;";
    },
  },
  created: function () {
    this.draftRefresh();
    this.championsRefresh();
  },
  methods: {
    draftStart() {
      const self = this;
      axios
        .post(
          "/draft/draft/" + roomCode,
          { no: "" },
          { xsrfCookieName: "csrftoken", xsrfHeaderName: "X-CSRFToken" }
        )
        .then(function (response) {
          draftSocket.send(JSON.stringify({ message: "championsrefresh|" }));
          draftSocket.send(JSON.stringify({ message: "draftrefresh|" }));
        });
    },
    championsRefresh() {
      const self = this;
      const lane = document.querySelector("input[name='lane']:checked")
        ? document.querySelector("input[name='lane']:checked").value
        : "";
      const name = document.querySelector("input[name='name']")
        ? document.querySelector("input[name='name']").value
        : "";
      const code = roomCode;
      axios
        .get("/draft/champion?lane=" + lane + "&name=" + name + "&code=" + code)
        .then(function (response) {
          self.championsList = response.data;
        });
    },
    draftRefresh() {
      const self = this;
      const now = Math.floor(Date.now() / 1000);
      axios.get("/draft/draft/" + roomCode).then(function (response) {
        if (response.data.blue_done) {
          self.laneBlue = true;
        }
        if (response.data.red_done) {
          self.laneRed = true;
        }
        if (response.data.timer) {
          if (master == roomId) {
            self.timer = now - response.data.timer;
            self.countDownTimer();
          }
          self.start = true;
        }
        self.championsValid = response.data.champions_valid;
        if (response.data.banpick) {
          banpick = response.data.banpick.split("/");
          self.draft.banpick = banpick;
          self.order = banpick.length;
          if (self.laneBlue && self.laneRed) {
            self.order++;
          }
          for (let i = 0; i < banpick.length; i++) {
            const el = document.querySelector(
              "#team_wrap .od_" + String(i) + " .sp"
            );
            if ([4, 5, 6 ,7, 12, 13, 14, 15].includes(i)) {
              el.style.backgroundImage = "url(/assets/img/genshin_all.png)";
              el.style.backgroundPosition =
                "0px -" + String(banpick[i] * 81) + "px";
            } else {
              if (banpick[i] == "999") {
                el.style.backgroundImage = "radial-gradient(black, #555555)";
                el.style.backgroundSize = "100% 100%";
              } else {
                if (self.order == 17) {
                  el.style.backgroundImage = "url(/assets/img/genshin_all.png)";
                  el.style.backgroundPosition =
                    "0px -" + String(banpick[i] * 81) + "px";
                } else {
                  el.style.backgroundImage = "url(/assets/img/genshin_all.png)";
                  el.style.backgroundPosition =
                    "0px -" + String(banpick[i] * 50.65) + "px";
                }
              }
            }
          }
        }
        if (document.querySelector(".team .container.now")) {
          document.querySelector(".team .container.now .order").innerHTML = "";
          document
            .querySelector(".team .container.now")
            .classList.remove("now");
        }
        if (document.querySelector(".team .container.next")) {
          document.querySelector(".team .container.next .order").innerHTML = "";
          document
            .querySelector(".team .container.next")
            .classList.remove("next");
        }
        if (self.order < 16) {
          document.querySelector(".od_" + self.order).classList.add("now");
          document.querySelector(".od_" + self.order + " .order").innerHTML =
            "选择中...";
        }
        if (self.order < 15) {
          document
            .querySelector(".od_" + String(self.order + 1))
            .classList.add("next");
          document.querySelector(
            ".od_" + String(self.order + 1) + " .order"
          ).innerHTML = "下一回合选择";
        }
        if (self.order >= 16) {
          clearInterval(self.timerF);
          self.timer = 30;
          self.laneChoice();
        }
        if (self.order == 17) {
          self.draftEnd();
        }
      });
    },
    draftSelect(no) {
      el2 = document.querySelector(".sp-" + String(no));
      if (el2.hasAttribute("disabled")) {
        return false;
      }
      this.draft.temp = String(no);
      el1 = document.querySelector(".sp.selected");
      if (el1) {
        el1.classList.remove("selected");
      }
      el2.classList.add("selected");
      if (
        [4, 5, 6, 7, 12, 13, 14, 15].includes(this.order) &&
        this.draft.team == team
      ) {
        draftSocket.send(
          JSON.stringify({
            message: "championselect|" + this.order + "," + String(no),
          })
        );
      }
    },
    draftChoice() {
      const self = this;
      let no = self.draft.temp;
      if (no) {
        const postData = { no };
        axios
          .post("/draft/draft/" + roomCode, postData, {
            xsrfCookieName: "csrftoken",
            xsrfHeaderName: "X-CSRFToken",
          })
          .then(function (response) {
            draftSocket.send(JSON.stringify({ message: "draftrefresh|" }));
            el = document.querySelector(".sp-" + no);
            if (document.querySelector("input[name='name']").value) {
              document.querySelector("input[name='name']").value == "";
            }
            if (document.querySelector("input[name='lane']:checked")) {
              document.querySelector(
                "input[name='lane']:checked"
              ).checked = false;
            }
            draftSocket.send(JSON.stringify({ message: "championsrefresh|" }));
            self.draft.temp = "";
          });
      }
    },
    laneChoice() {
      if (team != "none") {
        const el_array = document.querySelectorAll(".lane .container");
        for (let i = 0; i < 4; i++) {
          const order = el_array[i].className.split("_")[1];
          const pick = this.draft.banpick[order];
          const el_sp = document.querySelector(".lane .od_" + order + " .sp");
          el_sp.style.backgroundImage = "url(/assets/img/genshin_all.png)";
          el_sp.style.backgroundPosition = "0px -" + String(pick * 100) + "px";
        }
      }
    },
    laneChoiceDone(team) {
      let postData = new FormData();
      let cnt = 0;
      // if (team == "blue") {
      //   for (let i = 0; i < 5; i++) {
      //     const temp = document.querySelector(
      //       "input[name='b" + i + "']:checked"
      //     );
      //     if (temp) {
      //       postData.append(i, temp.value);
      //       cnt++;
      //     } else {
      //       alert("请选择所有.");
      //       break;
      //     }
      //   }
      // }
      // if (team == "red") {
      //   for (let i = 0; i < 5; i++) {
      //     const temp = document.querySelector(
      //       "input[name='r" + i + "']:checked"
      //     );
      //     if (temp) {
      //       postData.append(i, temp.value);
      //       cnt++;
      //     } else {
      //       alert("请选择所有行.");
      //       break;
      //     }
      //   }
      // }
      postData.append("team", team);
      axios
          .post("/draft/lane/" + roomCode, postData, {
            xsrfCookieName: "csrftoken",
            xsrfHeaderName: "X-CSRFToken",
          })
          .then(function (response) {
            draftSocket.send(JSON.stringify({ message: "draftrefresh|" }));
            // if (response.data == "error") {
            //   alert("有重叠的选择.");
            //   return false;
            // } else {
            //   draftSocket.send(JSON.stringify({ message: "draftrefresh|" }));
            // }
          });
      // if (cnt == 5) {
      //   axios
      //     .post("/draft/lane/" + roomCode, postData, {
      //       xsrfCookieName: "csrftoken",
      //       xsrfHeaderName: "X-CSRFToken",
      //     })
      //     .then(function (response) {
      //       if (response.data == "error") {
      //         alert("有重叠的选择.");
      //         return false;
      //       } else {
      //         draftSocket.send(JSON.stringify({ message: "draftrefresh|" }));
      //       }
      //     });
      // }
    },
    draftEnd() {},
    countDown() {
      timer = this.timer + 1;
      draftSocket.send(
        JSON.stringify({
          message: "timer|" + String(timer),
        })
      );
    },
    countDownTimer() {
      if (this.timerF) {
        return false;
      } else {
        this.timerF = setInterval(this.countDown, 1000);
      }
    },
  },
});
