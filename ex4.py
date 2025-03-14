import time

# ฟังก์ชัน Quick Sort ที่เลือก pivot โดยใช้ Median of Three
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # เลือก pivot โดยใช้การเปรียบเทียบตำแหน่งแรก, ตำแหน่งกลาง และตำแหน่งสุดท้าย
    first = arr[0]
    last = arr[-1]
    middle = arr[len(arr) // 2]
    
    # ใช้ median of three เพื่อเลือก pivot
    pivot = sorted([first, middle, last])[1]  # เลือกค่ากลางจากสามค่าที่เปรียบเทียบ
    
    # แบ่งข้อมูลเป็นสองส่วน
    left = [x for x in arr if x < pivot]  # ใช้ < แทน <= เพื่อหลีกเลี่ยงค่าที่เท่ากับ pivot
    right = [x for x in arr if x > pivot]  # ใช้ > แทน >= เพื่อหลีกเลี่ยงค่าที่เท่ากับ pivot
    
    # รวมผลลัพธ์
    return quick_sort(left) + [pivot] + quick_sort(right)

# ทดสอบ Quick Sort
test_data = [64, 34, 25, 12, 22, 11, 45, 24, 6, 90]
print("ข้อมูลก่อนเรียง:", test_data)

start_time = time.time()
sorted_data = quick_sort(test_data.copy())
end_time = time.time()

print("ข้อมูลหลังเรียง:", sorted_data)
print(f"เวลาที่ใช้: {(end_time - start_time)*1000:.6f} มิลลิวินาที")

# ฟังก์ชัน Quick Sort พร้อมการแสดงขั้นตอน
def quick_sort_with_steps(arr, depth=0):
    indent = "  " * depth
    print(f"{indent}quick_sort({arr})")
    
    if len(arr) <= 1:
        print(f"{indent}ข้อมูลมีขนาด <= 1, ส่งคืน {arr}")
        return arr
    
    first = arr[0]
    last = arr[-1]
    middle = arr[len(arr) // 2]
    
    # ใช้ median of three เพื่อเลือก pivot
    pivot = sorted([first, middle, last])[1]
    print(f"{indent}เลือก pivot = {pivot} (จาก {first}, {middle}, {last})")
    
    left = [x for x in arr if x < pivot]  # ใช้ < แทน <=
    right = [x for x in arr if x > pivot]  # ใช้ > แทน >=
    
    print(f"{indent}แบ่งข้อมูล: left = {left}, right = {right}")
    
    result = quick_sort_with_steps(left, depth + 1) + [pivot] + quick_sort_with_steps(right, depth + 1)
    print(f"{indent}ผลลัพธ์รวม: {result}")
    
    return result

# ทดสอบแสดงขั้นตอน
test_data = [64, 34, 25, 12, 22, 11, 45, 24, 6, 90]
quick_sort_with_steps(test_data.copy())
