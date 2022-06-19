module PlottingPractice

import Base.show

export iter, levy_c

A₀ = [0 1;0 0]

function levyc₁(A)
    return  [.5 -.5;.5 .5] * A
end

function levyc₂(A)
    return [.5 .5;-.5 .5] * A .+ [.5; .5]
end

functions = [levyc₁, levyc₂]

"""
    function(i::Int)

Returns an array that is a subset of the Levy C IFS

```jldoctest
julia> iter(1)  
2×4 Matrix{Float64}:  
 0.0  0.5  0.5  1.0  
 0.0  0.5  0.5  0.0  
```
"""
function iter(i::Integer)::Matrix{Float64}
    A = [0 1;0 0]
    for _ = 1:i
        A = [levyc₁(A) levyc₂(A)]
    end
    return A
end

mutable struct Fractal
    A::Matrix{Float64}
    functions::Vector{Function}
    iters::Integer
end # struct 

function iter(f::Fractal, i::Integer)::Matrix{Float64}
    A = f.A
    for _ = 1:i
        A = [f.functions[1](A) f.functions[2](A)]
    end
    return A
end

function show(io::IO, x::Fractal)
    print(io, ) 
end

levy_c = Fractal(iter(1), [levyc₁, levyc₂], 1)
# print(levy_c)

end # module
