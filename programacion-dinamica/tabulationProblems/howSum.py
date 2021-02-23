# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # How Sum Problem - Tabulation Solution
# Write a function 'how_sum(target_sum,numbers)' that takes in a target sum and an array of numbers as arguments.
# The function shuld return an array containing any combination of elements that add up to exactly of target_sum using numbers from the array.
# Constraints:
# - If there is no combination that adds up to the target_sum, then return null.
# - If there are multiple combinations possible, you may return any single one.
# - You may use an element of the array as many times as needed.
# - You may assume that all inpot numbers are nonnegative.

# %%
def how_sum(target_sum, numbers):
    table = [None] * (target_sum + 1)
    table[0] = []

    for i in range(target_sum+1):
        if table[i] is not None:
            for num in numbers:
                if i+num <= target_sum:
                    table[i+num] = table[i]+[num]

    return table[target_sum]

# %% [markdown]
# ***
# ## Tests
# ### How sum `7` whith the list `[2,3]` should return `[3, 2, 2]`


# %%
print(f"How sum 7 the list [2,3]: {how_sum(7,[2,3])}")

# %% [markdown]
# ### How sum `7` whith the list `[5,3,4,7]` should return `[4, 3]`

# %%
print(f"How sum 7 the list [5,3,4,7]: {how_sum(7,[5,3,4,7])}")

# %% [markdown]
# ### How sum `7` whith the list `[2,4]` should return `None`

# %%
print(f"How sum 7 the list [2,4]: {how_sum(7,[2,4])}")

# %% [markdown]
# ### How sum `8` whith the list `[2,3,5]` should return `[2,2,2,2]`

# %%
print(f"How sum 8 the list [2,3,5]: {how_sum(8,[2,3,5])}")

# %% [markdown]
# ### How sum `300` whith the list `[7,14]` should return `None`

# %%
print(f"How sum 300 the list [7,14]: {how_sum(300,[7,14])}")
