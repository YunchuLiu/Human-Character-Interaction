import utility 


mapping={'joint2':['left_shoulder_','left_elbow_','left_hand_'],'joint4':['torso_', 'left_hip_', 'left_knee_'],'joint5':['left_hip_', 'left_knee_','left_foot_'],'joint6':['torso_', 'right_hip_','right_knee_'],
'joint7':['right_hip_', 'right_knee_','right_foot_'],'joint9':['torso_', 'left_hip_','left_foot_'],'joint10':['head_', 'neck_','torso_']}



def main():
    joint_state=[]
    
    for i in range (1,10):
            torso_id= "torso_"+str(i)
            if frameExists(torso_id):
                ID=str(i)
                break
    
    ID=str(1)
               
    for key in mapping:
        
        a=get_trans(mapping[key][0]+ID,mapping[key][1]+ID)
        b=get_trans(mapping[key][1]+ID,mapping[key][2]+ID)
        theta=get_theta(a,b)
        joint_state.append((key,theta))
        
        
    d=dict(joint_state)
    print d 
        
        
        
        
        
main()
 








