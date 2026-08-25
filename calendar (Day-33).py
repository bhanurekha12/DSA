#activity selection valid timing:
'''n=int(input("Enter number of activities: "))
activities=[]
for i in range(n):
    s=int(input(f"enter start time of activity{i+1}: "))
    e=int(input(f"enter end time of acitvity{i+1}: "))
    activities.append((s,e))
activities.sort(key=lambda x:x[1])
print("\n selected activities: ")
last_finish=-1
for activity in activities:
    if activity[0] >=last_finish:
        print(activity)
        last_finish=activity[1]'''