def check_inputs(log_file_path="expected/Task_4/sorted_in3_results.out"):
    f = open('outs/a2_starter_code_output_hadoop/in3_output_task4______spark.out/part-00000')
    # f = open('outs/a2_starter_code_output_hadoop/in3_output_task4.out/part-r-00000')
    d = {}
    e = {}
    # outs/a2_starter_code_output_hadoop/in0_output_task1______spark.out
    # print(f.read(), "our ouptut")
    for line in f:
        if line == '\n':
            continue
        chunks = line.split(",")
        d[",".join(chunks[:2])] = chunks[-1]
    f.close()

    f = open(log_file_path)
    # print(f.read(), "expected ouptut")
    
    line_count = 0
    
    for line in f:
        chunks = line.split(",")
        e[",".join(chunks[:2])] = chunks[-1]
    f.close()
    if e == d: 
        print("hi")
    else: 
        print(len(e))
        print(len(d))
        # print(d)
    # for line in f:
    #     chunks = line.split(",")
    #     line_count += 1

    #     correct_value = d[",".join(chunks[:2])]

    #     if correct_value != chunks[-1]:
    #         print(f"[ERR]: Mismatched values! Correct value: {correct_value}, our value: {chunks[-1]}")

    # if line_count != len(d.keys()):
    #     print("[ERR]: Unequal lines!")

    # print("Finished.")
    # f.close()

if __name__ == "__main__":
    check_inputs()



