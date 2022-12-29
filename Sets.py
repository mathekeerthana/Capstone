# superset,subset,dis jointset

set_s={1,2,3,4,5,6}
set_s1={4,5}
super_set=set_s.issuperset(set_s1)
print(super_set)

sub_set=set_s.issubset(set_s1)
print(sub_set)

dis_joint=set_s.isdisjoint(set_s1)
print(dis_joint)

# print common elements in 3 sets

set_1={1,'s','r',2,7,'t','h'}
set_2={'s',3,6,7,'g'}
set_3={'s',7}
set_intersection=set_1 &set_2 & set_3
print(set_intersection)

# print numbers that are present in both the lines

set_f ={1,2,3,4,5}
set_g ={4,5,6,7,8}
set_intersection=set_f & set_g
print(set_intersection)
