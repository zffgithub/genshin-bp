#! /bin/bash
if [ 0"$FLASK_CODE_DIR" = "0" ];then
    export FLASK_CODE_DIR="."
    export FLASK_APPLOGS_DIR="."
    export FLASK_PRIVDATA_DIR="."
fi

HOST=`ifconfig | grep broadcast | grep -v '0.0.0.0' |awk -F ' ' -v OFS=',' '{print $2}'`

if [ 0"$ENVTYPE" = "0" ];then
    export ENVTYPE="$1"
fi
echo "condition is: "$ENVTYPE

ip_num=`echo $HOST | awk '{print NF}'`


if [ 0"$FLASK_PRIVDATA_DIR" = "0." -o -z "$FLASK_PRIVDATA_DIR" ];then
    venv_loc="."
    # 如果不存在这些变量，使用当前目录存储
fi

#GOOGLECHROME_PATH = "./google-chrome-stable_current_amd64.deb"

if [ "prod" = "$ENVTYPE" ];then
    # ubuntu18.04.1
    if [ "$USER" = "ubuntu" ];then
        virtual=python3
        sudo unlink /bin/sh
        sudo ln -s /bin/bash /bin/sh
        sudo apt-get update
#        sudo apt-get install -y python3-venv
        sudo apt-get install -y python3.8-venv
        source /etc/profile
    else
        virtual=python3
        sudo unlink /bin/sh
        sudo ln -s /bin/bash /bin/sh
        sudo apt-get update
        sudo apt-get install -y cloud-utils # 获取instance_id
#        sudo apt-get install -y python3-venv
        sudo apt-get install -y python3.8-venv
        source /etc/profile
    fi
elif [ "dev" = "$ENVTYPE" ];then
    if [ "$USER" = "ubuntu" ];then
        virtual=python3
    else
        virtual=python3
    fi
elif [ "$ENVTYPE" = "test" ];then
    virtual=python3
fi

echo "installing: ENVTYPE=${ENVTYPE} in: ${USER}"

if [ "$venv_loc" = "." ];then
    # ubuntu 的默认环境需要
    # sudo apt-get install python3.7-venv
    echo 'virtual:' $virtual
    $virtual -m venv $venv_loc/.env
    source $venv_loc/.env/bin/activate
    pip install --upgrade pip
    #pip3 install -r $venv_loc/requirements.txt -i https://pypi.douban.com/simple/ > /dev/null 2>&1
    pip3 install -r $venv_loc/requirements.txt -i https://pypi.douban.com/simple/
    deactivate
    echo "installed: offline"
    #echo "$ENVTYPE" > $venv_loc/env_flag.in
else
    $virtual -m venv $FLASK_PRIVDATA_DIR/.env
    source $FLASK_PRIVDATA_DIR/.env/bin/activate
    pip3 install -r  $FLASK_CODE_DIR/requirements.txt -i https://pypi.douban.com/simple/ > /dev/null 2>&1
    deactivate
    echo "installed: online"
    #echo "$ENVTYPE" > $FLASK_PRIVDATA_DIR/env_flag.in
fi
