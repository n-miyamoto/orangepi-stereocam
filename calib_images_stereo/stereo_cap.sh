#!/bin/bash

if [ $# -ne 1 ]; then
  echo "./stereo_capture.sh <image_name>"
  exit 1
fi

v4l2-ctl -d /dev/video0 --set-ctrl 'exposure=1660,analogue_gain=248'
v4l2-ctl -d /dev/video5 --set-ctrl 'exposure=1660,analogue_gain=248'

gst-launch-1.0 v4l2src device=/dev/video0 num-buffers=1  ! videoconvert ! video/x-raw,format=NV12,width=1920,height=1080,framerate=30/1 ! jpegenc ! filesink location=$1-left.jpg &
gst-launch-1.0 v4l2src device=/dev/video5 num-buffers=1  ! videoconvert ! video/x-raw,format=NV12,width=1920,height=1080,framerate=30/1 ! jpegenc ! filesink location=$1-right.jpg &

