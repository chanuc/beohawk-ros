#include <ros/ros.h>
#include <sensor_msgs/Image.h>
#include <boost/shared_ptr.hpp>
#include <opencv2/video/video.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>

using namespace std;
using boost::shared_ptr;

class OpticalFlow
{
  ros::NodeHandle nh;

  ros::Subscriber sub_rawimage;
  uint counter_sub_rawimage;

  cv::Mat image_old, image_new, image_result;
  shared_ptr<vector<cv::Point2f> > points_old, points_new;

 public:
  OpticalFlow (ros::NodeHandle& _nh): nh(_nh), counter_sub_rawimage(0),
               points_old(new vector<cv::Point2f>()), points_new(new vector<cv::Point2f>())
  {
    sub_rawimage = nh.subscribe("/camera/image_mono", 100,
                                &OpticalFlow::callback_sub_rawimage, this);
    cv::namedWindow("img1");
    cv::namedWindow("img2");
  }

  void callback_sub_rawimage (const sensor_msgs::Image::ConstPtr& msg_rawimage)
  {
    // Convert the image into OpenCV format, and prepare
    cv::resize(cv::Mat(480, 640, CV_8UC1, (char*) &(msg_rawimage->data[0])), image_new, cv::Size(320,240));
    
    // Do optical flow and PNP solving
    if (counter_sub_rawimage != 0) {
     
      // Find features for one image.
      cv::goodFeaturesToTrack(image_old, *points_old, 75, 0.25, 0.1);
     
      // Find corresponding feature for the other image.
      vector<uchar> status; vector<float> error;
      cv::calcOpticalFlowPyrLK(image_old, image_new, *points_old, *points_new, status, error);

      //cv::Vector3 tvec, rvec;
      //cv::solvePnPRansac(*points_old, *points_new, cv::eye(3), null, rvec, tvec);
      
      // Print output.
      if (counter_sub_rawimage % 10 == 1) image_result = cv::Mat(240, 320, CV_8UC1, cv::Scalar(0));
      for (size_t i = 0; i < status.size(); i++)
      {
        if (status[i] == 0) continue;
        else cv::line(image_result, points_old->at(i), points_new->at(i), cv::Scalar(255));
      }
      cv::imshow("result", image_result);
      cv::waitKey(2);
    }

    image_old = image_new;
    ++ counter_sub_rawimage;
  }
};

int main (int argc, char** argv)
{
  ros::init(argc, argv, "optical_flow_node");
  ros::NodeHandle nh;
  OpticalFlow optical_flow(nh);
  ros::spin();
  return 0;
}

