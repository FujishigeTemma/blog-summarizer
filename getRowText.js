function getRowText(tree) {
    if (tree.children.length <= 0) return tree

    const queue = [...tree.children]
    let now
    while (queue.length > 0) {
        now = queue.shift()
        if (now.tagName == "CODE") {
            now.remove()
        } else {
            queue.push(...now.children)
        }
    }
    return tree
}
getRowText(document.getElementsByTagName("article")[0]).innerText