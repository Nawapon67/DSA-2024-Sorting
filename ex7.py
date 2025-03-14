import random
import time
import matplotlib.pyplot as plt
import sorting

def compare_sort():
    # ทดสอบกับขนาดข้อมูลต่างๆ
    sizes = [100,500, 1000, 5000, 10000, 20000]
    bubble_times = []
    insertion_times = []
    selection_times =[]
    
    for size in sizes:
        # สร้างชุดข้อมูลแบบสุ่มในช่วง 0-999
        data = [random.randint(0, 9999) for _ in range(size)]
        
        # วัดเวลา bubble Sort
        start_time = time.time()
        sorttype.bubble_sort(data.copy())
        bubble_times.append((time.time() - start_time) * 1000)
        
        # วัดเวลา insertion Sort
        start_time = time.time()
        sorttype.insertion_sort(data.copy())
        insertion_times.append((time.time() - start_time) * 1000)

            # วัดเวลา selection Sort
        start_time = time.time()
        sorttype.selection_sort(data.copy())
        selection_times.append((time.time() - start_time) * 1000)

        print(f"ขนาดข้อมูล {size}:")
        print(f"  Bubble Sort: {bubble_times[-1]:.2f} มิลลิวินาที")
        print(f"  Insertion Sort: {insertion_times[-1]:.2f} มิลลิวินาที")
        print(f"  Selection Sort: {selection_times[-1]:.2f} มิลลิวินาที")

    # แสดงผลลัพธ์เป็นกราฟ
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, bubble_times, marker='o', label='Bubble Sort')
    plt.plot(sizes, insertion_times, marker='d', label='Insertion Sort')
    plt.plot(sizes, selection_times, marker='s', label='Selection Sort')
    plt.title('Performance comparison of sorting (Data 0-999). Created By [Student Name]')
    plt.xlabel('Input Size')
    plt.ylabel('Time (Milliseconds)')
    plt.legend()
    plt.grid(True)
    plt.savefig('Performance.png')
    plt.show()

# เปรียบเทียบประสิทธิภาพ
sorttype=sorting

compare_sort()