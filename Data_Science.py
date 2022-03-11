# -------------------------#
#         Numpy            #
# -------------------------#
import numpy as np

heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]
# cont = 0
# for height in heights:
#     if height>188:
#         cont+=1
# print (cont)

heights_arr = np.array(heights)
print((heights_arr>188).sum())
print(heights_arr.size)
print(heights_arr.shape)

ages = [57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 49, 64, 50, 48, 65, 52, 56, 46, 54, 49, 51, 47, 55, 55, 54, 42, 51, 56, 55, 51, 54, 51, 60, 62, 43, 55, 56, 61, 52, 69, 64, 46, 54, 47, 70]

heights_and_ages =heights+ages
print(heights_and_ages)
heights_and_ages_arr = np.array(heights_and_ages)
# print(heights_and_ages_arr)
print(heights_and_ages_arr.shape)
heights_and_ages_arr =heights_and_ages_arr.reshape(2,45)
print(heights_and_ages_arr.dtype)
print(heights_and_ages_arr.shape)

# Indexing
print(heights_arr[2])
print(heights_and_ages_arr[1][2])

# Slicing

print(heights_and_ages_arr[0, 0:3])
print(heights_and_ages_arr[1, :4])
print(heights_and_ages_arr[: ,3])

# Assigning Values
heights_arr[3]= 165
heights_and_ages_arr[0,3]=165
heights_and_ages_arr[:2, :2] = 0
print(heights_and_ages_arr)

# Assigning array to array
heights_and_ages_arr[:,0]=[198, 58]
print(heights_and_ages_arr)

newRecord = np.array([[180,183,190],[54,50,69]])
print(newRecord)
heights_and_ages_arr[:,42:] = newRecord
print(heights_and_ages_arr)

# Combining Two Arrays

ages_arr = np.array(ages)
print(ages_arr.shape)
print(ages_arr[:3,])

heights_arr = heights_arr.reshape(45,1)
ages_arr = ages_arr.reshape(45,1)

height_and_age_arr = np.hstack((heights_arr,ages_arr))
print(height_and_age_arr)

heights_arr = heights_arr.reshape(45,1)
ages_arr = ages_arr.reshape(45,1)

height_and_age_arr = np.vstack((heights_arr,ages_arr))
print(height_and_age_arr)
print(height_and_age_arr[:,:3])

height_and_age_arr = np.concatenate((heights_arr,ages_arr),axis=1)
print(height_and_age_arr)

# Operations
# height_and_age_arr = height_and_age_arr.reshape(45,1)
print(height_and_age_arr[: , 0]*0.0328084)
print(height_and_age_arr.sum())
print(height_and_age_arr.sum(axis = 0))
print(height_and_age_arr.sum(axis=1))
print(height_and_age_arr.min(axis=0))

# Comparisons
print(height_and_age_arr[:, 1]<55)
print((height_and_age_arr[:,1]==51).sum())

# Masking ans Subsetting

mask= height_and_age_arr[:,0]>=182
print(mask.sum())

tall_presidents = height_and_age_arr[mask]
print(tall_presidents.shape)

# Multiple Criteria
mask=(height_and_age_arr[:,0]>=182)&(height_and_age_arr[:,1]<=50)
print(height_and_age_arr[mask])

# Data Science - Average of Rows
# -----------------------------#
#            PANDAS            #
#------------------------------#
# importing pandas


# Series
# print(pd.Series([1, 2, 3], index=['a', 'b', 'c'])) # with index