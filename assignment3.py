import cv2
print("1.make video")
print("2.See video")
choice=int(input("Enter a number: "))
match choice:
    case 1:
        cap=cv2.VideoCapture(0)
        while True:
            ret,frame=cap.read()
            if ret==False:
                break
            cv2.imshow("Video Frame",frame)
            if cv2.waitKey(1) & 0xFF==ord('q'):
                break
            width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            codec=cv2.VideoWriter_fourcc(*'XVID')
            cv2.VideoWriter('output.avi',codec,20.0,(width,height))
        cap.release()
        cv2.destroyAllWindows()
    case 2:
        cap=cv2.VideoCapture('output.avi')
        while cap.isOpened():
            ret,frame=cap.read()
            if ret==True:
                cv2.imshow("Video Frame",frame)
                if cv2.waitKey(25) & 0xFF==ord('q'):
                    break
            else:
                break
        cap.release()
        cv2.destroyAllWindows()