import pandas as pd
import plotly.figure_factory as ff
import statistics
import random
import plotly.graph_objects as go

df = pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()

#population_mean = statistics.mean(data)
#print("The population mean is ", population_mean)

#population_std = statistics.stdev(data)
#print("The population standard deviation is ", population_std)

def random_set_of_means(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index] 
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

mean_list = []
for i in range(0, 1000):
    set_of_means = random_set_of_means(100)
    mean_list.append(set_of_means)

sampling_mean = statistics.mean(mean_list)
#print("The sampling mean is ", sampling_mean)

sampling_std = statistics.stdev(mean_list)
#print("The sampling standard deviation is ", sampling_std)

#fig = ff.create_distplot([mean_list], ["student score"], show_hist = False)
#fig.add_trace(go.Scatter(x = [sampling_mean, sampling_mean], y = [0, 0.2], mode = "lines", name = "Mean"))
#fig.show()

# finding standard deviation's starting and ending values 
first_std_start, first_std_end = sampling_mean - sampling_std, sampling_mean + sampling_std
second_std_start, second_std_end = sampling_mean - 2*sampling_std, sampling_mean + 2*sampling_std
third_std_start, third_std_end = sampling_mean - 3*sampling_std, sampling_mean + 3*sampling_std
print("Std1 ", first_std_start, first_std_end)
print("std2 ", second_std_start, second_std_end)
print("std3 ", third_std_start, third_std_end)

#fig = ff.create_distplot([mean_list], ["student marks"], show_hist= False)
#fig.add_trace(go.Scatter(x = [sampling_mean, sampling_mean], y = [0, 0.2], mode = "lines", name= "mean"))
#fig.add_trace(go.Scatter(x = [first_std_start, first_std_start], y = [0, 0.2], mode = "lines", name= "std 1 start"))
#fig.add_trace(go.Scatter(x = [first_std_end, first_std_end], y = [0, 0.2], mode = "lines", name= "std 1 end"))
#fig.add_trace(go.Scatter(x = [second_std_start, second_std_start], y = [0, 0.2], mode = "lines", name= "std 2 start"))
#fig.add_trace(go.Scatter(x = [second_std_end, second_std_end], y = [0, 0.2], mode = "lines", name= "std 2 end"))
#fig.add_trace(go.Scatter(x = [third_std_start, third_std_start], y = [0, 0.2], mode = "lines", name= "std 3 start"))
#fig.add_trace(go.Scatter(x = [third_std_end, third_std_end], y = [0, 0.2], mode = "lines", name= "std 3 end"))
#fig.show()"

df1 = pd.read_csv("data1.csv")
data1 = df1["Math_score"].tolist()
mean_of_sample_1 = statistics.mean(data1)
#print("The mean of the first sample is ", mean_of_sample_1)

#fig = ff.create_distplot([mean_list], ["student marks"], show_hist= False)
#fig.add_trace(go.Scatter(x = [sampling_mean, sampling_mean], y = [0, 0.2], mode = "lines", name= "mean"))
#fig.add_trace(go.Scatter(x = [mean_of_sample_1, mean_of_sample_1], y = [0, 0.2], mode = "lines", name= "sample mean 1"))
#fig.add_trace(go.Scatter(x = [first_std_end, first_std_end], y = [0, 0.2], mode = "lines", name= "std 1 end"))
#fig.add_trace(go.Scatter(x = [second_std_end, second_std_end], y = [0, 0.2], mode = "lines", name= "std 2 end"))
#fig.add_trace(go.Scatter(x = [third_std_end, third_std_end], y = [0, 0.2], mode = "lines", name= "std 3 end"))
#fig.show()

df2 = pd.read_csv("data2.csv")
data2 = df2["Math_score"].tolist()
mean_of_sample_2 = statistics.mean(data2)
#print("The mean of the second sample is ", mean_of_sample_2)

#fig = ff.create_distplot([mean_list], ["student marks"], show_hist= False)
#fig.add_trace(go.Scatter(x = [sampling_mean, sampling_mean], y = [0, 0.2], mode = "lines", name= "mean"))
#fig.add_trace(go.Scatter(x = [mean_of_sample_2, mean_of_sample_2], y = [0, 0.2], mode = "lines", name= "sample mean 2"))
#fig.add_trace(go.Scatter(x = [first_std_end, first_std_end], y = [0, 0.2], mode = "lines", name= "std 1 end"))
#fig.add_trace(go.Scatter(x = [second_std_end, second_std_end], y = [0, 0.2], mode = "lines", name= "std 2 end"))
#fig.add_trace(go.Scatter(x = [third_std_end, third_std_end], y = [0, 0.2], mode = "lines", name= "std 3 end"))
#fig.show()

df3 = pd.read_csv("data3.csv")
data3 = df3["Math_score"].tolist()
mean_of_sample_3 = statistics.mean(data3)
print("The mean of the third sample is ", mean_of_sample_3)

#fig = ff.create_distplot([mean_list], ["student marks"], show_hist= False)
#fig.add_trace(go.Scatter(x = [sampling_mean, sampling_mean], y = [0, 0.2], mode = "lines", name= "mean"))
#fig.add_trace(go.Scatter(x = [mean_of_sample_3, mean_of_sample_3], y = [0, 0.2], mode = "lines", name= "sample mean 3"))
#fig.add_trace(go.Scatter(x = [first_std_end, first_std_end], y = [0, 0.2], mode = "lines", name= "std 1 end"))
#fig.add_trace(go.Scatter(x = [second_std_end, second_std_end], y = [0, 0.2], mode = "lines", name= "std 2 end"))
#fig.add_trace(go.Scatter(x = [third_std_end, third_std_end], y = [0, 0.2], mode = "lines", name= "std 3 end"))
#fig.show()

z_score1 = (mean_of_sample_1 - sampling_mean) /sampling_std
print("The first z score is", z_score1)

z_score2 = (mean_of_sample_2 - sampling_mean) /sampling_std
print("The second z score is", z_score2)

z_score3 = (mean_of_sample_3 - sampling_mean) / sampling_std
print("The third z score is", z_score3)