#include <ros/ros.h>
#include <tf/transform_broadcaster.h>
#include <geometry_msgs/Vector3Stamped.h>

using namespace std;

ros::Publisher pub;

void hahacallback (const geometry_msgs::Vector3::ConstPtr& msg)
{
  geometry_msgs::Vector3Stamped vec;
  vec.vector = *msg;
  vector.header.stamp = ros::Time::now();
  pub.publish(vec);
  
  static tf::TransformBroadcaster br;
  tf::Transform trafo;
  trafo.setOrigin(tf::Vector3(0,0,0));
  trafo.setRotation(tf::Quaternion(msg->x, msg->y, msg->z));
  br.sendTransform(tf::StampedTransform(trafo, ros::Time::now(), "/world", "/laser"));
}

int main (int argc, char** argv)
{
  ros::init(argc, argv, "abcdefg");
  ros::NodeHandle nh;
  pub = nh.publish<geometry_msgs::Vector3Stamped>("/angle", 10);
  ros::Subscriber sub = nh.subscribe("/haha", 10, hahacallback);
  ros::spin();
  return 0;
}