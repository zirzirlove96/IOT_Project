export STREAMER_PATH=$HOME/mjpg/mjpg-streamer/mjpg-streamer-experimental

export LD_LIBRARY_PATH=$STREAMER_PATH
$STREAMER_PATH/mjpg_streamer -i "input_raspicam.so" -o "output_http.so -p 8091 -w $STREAMER_PATH/www"
