#! /bin/bash
export LANG='UTC-8'
export LC_ALL='en_US.UTF-8'

echo "FLASK_CODE_DIR:" "$FLASK_CODE_DIR"
case $2 in
    dev)
        echo ""
        ;;
    prod)
        echo ""
        ;;
    *)
        echo "Using option{dev|prod}"
        exit
    ;;
esac


if [ 0"$FLASK_CODE_DIR" = "0" ];then
    export FLASK_CODE_DIR="`pwd`"
    export FLASK_APPLOGS_DIR="."
    export FLASK_PRIVDATA_DIR="."
fi


LOG_FILE=$FLASK_APPLOGS_DIR/log
if [ ! -e $LOG_FILE ];then
    mkdir $LOG_FILE
fi
if [ 0"$ENVTYPE" = "0" ];then
    export ENVTYPE="$2"
fi
echo "condition is: "$ENVTYPE

case $1 in
    install)
        echo "virtual env install python packages"
        sh $FLASK_CODE_DIR/bin/install.sh $2
    ;;
    start)
        echo "run start ... "$FLASK_PRIVDATA_DIR
        source $FLASK_PRIVDATA_DIR/.env/bin/activate
            cd $FLASK_CODE_DIR
        $FLASK_PRIVDATA_DIR/.env/bin/gunicorn \
                --pid=$LOG_FILE/run.pid \
                --config bin/gunicorn_config.py \
                --daemon app.flaske:app \
        deactivate
        echo "start with nohup"
    ;;
    run)
        echo "virtual env install python packages"
#        sh $FLASK_CODE_DIR/bin/install.sh $2
        source $FLASK_PRIVDATA_DIR/.env/bin/activate
            cd $FLASK_CODE_DIR
        $FLASK_PRIVDATA_DIR/.env/bin/gunicorn \
                --pid=$LOG_FILE/run.pid \
                --config bin/gunicorn_config.py \
                app.flaske:app
    ;;
    stop)
        PID_FILE=$LOG_FILE/run.pid
        if [ -e $PID_FILE ];then
            kill -15 `cat $PID_FILE`
            if [ $? = 0 ];then
                echo "stop server success"
            else
                echo "stop server failed"
            fi
        else
            echo "server is not started"
        fi
    ;;
    *)
        echo "Using option{install|start|run|stop}"
    ;;
esac
