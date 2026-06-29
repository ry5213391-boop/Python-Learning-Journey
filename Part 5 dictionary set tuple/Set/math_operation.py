s1 = {"eng", "hindi", "math", "cs", "physics", "chemistry"}
s2 = {"eng", "hindi", "bio", "cs", "physics", "chemistry"}
s3 = {'eng', "hindi", "math", "bio", "sanskrit", "chemistry"}
#print(s1, s2, type(s1), type(s2))
'''
# common subjects of student1 and student2 -> intersection
# common -> intersection

common_subjects = s1.intersection(s2, s3)

print(common_subjects)

# amphercent also used for intersection
common_subjects = s1 & s2
print(common_subjects)

'''
'''
# union -> for all subjects but duplicates are removed
all_sub = s1.union(s2, s3)
print(all_sub)
all_su = s1 | s2 | s3
print(all_su)
'''

days = {"mon", "tue", "thu", "fri", "sat", "sun"}
weekdays = {"sat", "sun"}

#difference od=f sets
weekdays = days - weekdays
print(weekdays)
# {'thu', 'fri', 'tue', 'mon'}
