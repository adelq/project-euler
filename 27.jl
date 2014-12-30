function quadratic_prime(a, b)
    return n -> n^2 + a*n + b
end

function isprime(n)
    if n < 0
        n *= -1
    end
    for i = 2:int(sqrt(n) + 1)
        if n % i == 0
            return false
        end
    end
    return true
end

function number_of_primes(f)
    prime = true
    n = 0
    while prime
        n += 1
        prime = isprime(f(n))
    end
    return n
end

max_primes = 0
max_a = 0
max_b = 0
for i = -999:999
    for j = -999:999
        current_primes = number_of_primes(quadratic_prime(i, j))
        if current_primes > max_primes
            max_primes = current_primes
            max_a = i
            max_b = j
        end
    end
end
println(max_a * max_b)
