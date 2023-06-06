from bvh_utils import *
# from viewer import SimpleViewer
# from Lab1_FK import *


def main():
    # one frame mocap data
    bvh = BVHMotion("./music_dance.bvh")
    # bvh.adjust_joint_name(name_list)
    translations, orientations = bvh.batch_forward_kinematics()
    T_pose = bvh.get_T_pose()
    print(translations.shape)

    # joint_name, translations1, orientations1 = part1_calculate_T_pose("./music_dance.bvh")
    # viewer = SimpleViewer()
    # viewer.show_pose(joint_name, translations, orientations)
    # viewer.run()


if __name__ == '__main__':
    main()
