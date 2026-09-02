basket_1={"apple","banana","carrot"}
basket_2={"apple","drumstick","apple"}
print(basket_2)
basket_2.add("eggplant")
print(basket_2)
commonword=basket_1.intersection(basket_2)
print(f"The common word in the sets is {commonword}")
print(basket_1)
import array as ray
a=ray.array("i",[0,1,1,2,3,5,8,13,21,34,55,89])
a.insert(3,100)
a.append(90)
a.count(3)
print(a)