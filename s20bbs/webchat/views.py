from django.contrib.auth.decorators import login_required
from django.shortcuts import render,HttpResponse

# Create your views here.
from webchat import models

import queue,json,time

GLOBAL_MSG_QUEUES = {

}

@login_required
def dashboard(request):

    return  render(request,"webchart/dashboard.html")

@login_required
def send_msg(request):
    print(request.POST)
    print(request.POST.get("msg"))
    msg_data = request.POST.get("data")
    #if request.POST.get()
    if msg_data :
        msg_data = json.loads(msg_data)
        msg_data['timestamp'] =  time.time()
        if msg_data['type'] == 'single':
            if not  GLOBAL_MSG_QUEUES.get(int(msg_data['to'])):
                GLOBAL_MSG_QUEUES[int(msg_data['to'])] = queue.Queue()
            GLOBAL_MSG_QUEUES[int(msg_data['to'])].put(msg_data)
    print(GLOBAL_MSG_QUEUES)
    return HttpResponse('msg---recevied')

    #if not GLOBAL_MSG_QUEUES.get()



def get_new_msgs(request):


    if request.user.userprofile.id not in GLOBAL_MSG_QUEUES:
        print("no queue for user [%s]" %request.user.userprofile.id,request.user)
        GLOBAL_MSG_QUEUES[request.user.userprofile.id] = queue.Queue()
    msg_count = GLOBAL_MSG_QUEUES[request.user.userprofile.id].qsize()
    q_obj = GLOBAL_MSG_QUEUES[request.user.userprofile.id]
    msg_list = []
    if msg_count >0:

        for msg in range(msg_count):
            msg_list.append(q_obj.get())

        print("new msgs:",msg_list)
    else:#没消息,要挂起
        print("no new msg for ",request.user,request.user.userprofile.id)
        #print(GLOBAL_MSG_QUEUES)

        try:
            msg_list.append(q_obj.get(timeout=60))
        except queue.Empty:
            print("\033[41;1mno msg for [%s][%s] ,timeout\033[0m" %(request.user.userprofile.id,request.user))
    return HttpResponse(json.dumps(msg_list))