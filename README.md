## orangepi_stereocam

## setup
```sh
sudo apt install v4l2 
sudo apt install v4l2-util
```

## 



camera settings
```sh
# show setting 
v4l2-ctl -d /dev/video0 -l 
v4l2-ctl -d /dev/video5 -l 

# left channel setting
v4l2-ctl -d /dev/video0 --set-ctrl 'exposure=1660,analogue_gain=248'
# right channel setting
v4l2-ctl -d /dev/video5 --set-ctrl 'exposure=1660,analogue_gain=248'
```

capture images
```sh
gst-launch-1.0 v4l2src device=/dev/video0 num-buffers=1  ! videoconvert ! video/x-raw,format=NV12,width=1920,height=1080,framerate=30/1 ! jpegenc ! filesink location=image-left.jpg 
gst-launch-1.0 v4l2src device=/dev/video5 num-buffers=1  ! videoconvert ! video/x-raw,format=NV12,width=1920,height=1080,framerate=30/1 ! jpegenc ! filesink location=image-right.jpg 
```


## reference 

- [Rockchip Linux Camera Developer Guide](https://dl.vamrs.com/products/rock960/docs/sw/Rockchip%C2%A0Linux%20Camera%C2%A0Developer%20Guide%20V1.1.pdf#page=46&zoom=100,61,68)
- [Rockchip Wiki](http://opensource.rock-chips.com/wiki_Rockchip-isp1)

