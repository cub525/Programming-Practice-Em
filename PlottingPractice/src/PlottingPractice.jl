module PlottingPractice

export greet, iter

function levyc₁(A)
    return  [.5 -.5;.5 .5] * A
end

function levyc₂(A)
    retur [.5 .5;-.5 .5] * A .+ [.5; .5]
end

function iter(i)
    A = [0 1;0 0]
    for _ = 1:i
        A = [levyc₁(A) levyc₂(A)]
    end
    return A
end

greet() = print("Hello World!")

end # module
