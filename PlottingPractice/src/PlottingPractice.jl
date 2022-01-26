module PlottingPractice

export iter

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
function iter(i)
    A = [0 1;0 0]
    for _ = 1:i
        A = [levyc₁(A) levyc₂(A)]
    end
    return A
end

end # module
