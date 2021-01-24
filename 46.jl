function isprime(n)
    for i = 2:int(sqrt(n) + 1)
        if n % i == 0
            return false
        end
    end
    return true
end

function isodd(n)
    return n % 2 == 1
end

function goldbach(prime, square)
    return prime + 2 * square
end

function istwicesquare(n)
    square = sqrt(n/2)
    return square == int(square)
end

primelist = filter(isprime, [1:10000])
result = 1
found = false

while !found
    result += 2
    j = 1
    found = true
    while j <= length(primelist) && result >= primelist[j]
        if istwicesquare(result - primelist[j])
            found = false
            break
        end
        j += 1
    end
end

println(result)
