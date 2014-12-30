# Upper bound for sums
limit = 28123

function isabundant(n)
    factor_sum = 0
    for i = 1:(n - 1)
        if n % i == 0
            factor_sum += i
        end
    end
    return factor_sum > n
end

# Array of all possible abundant numbers
all_abundants = filter(isabundant, [1:limit])

# Create array of whether an integer can be expressed as a sum of 2 abundants
sumOfAbundant = falses(limit)
for i = all_abundants
    for j = all_abundants
        if i + j <= limit
            sumOfAbundant[i + j] = true
        else
            break
        end
    end
end

# Sum up integers that cannot be expressed as sum of abundants
sum = 0
for (index, value) in enumerate(sumOfAbundant)
    if !value
        sum += index
    end
end
println(sum)
