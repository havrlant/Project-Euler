exports.all = (fun, list) ->
    for x in list when not fun(x)
        return false
    return true