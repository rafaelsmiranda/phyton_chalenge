def pagination(current_page=1, total_pages=10, boundaries=1, around=0):
    left_boundary = [1]
    right_boundary = []
    around_pages = []

    if current_page > total_pages:
        return "Current page exceeds total number of pages"

    for i in range(0, boundaries + 1):
        if i == 0:
            continue
        if i not in left_boundary:
            left_boundary.append(i)

    for i in range(current_page - around, current_page + around + 1):
        around_pages.append(i)

    for i in range(total_pages - boundaries, total_pages - 1):
        if i > around_pages[-1]:
            right_boundary.append(i+1)

    right_boundary.append(total_pages)

    pages = left_boundary
    pagination = []

    for i, page in enumerate(around_pages):
        if i == 0 and around_pages[i] < total_pages:
            pages.append(page)
            continue
        if (around_pages[i] > total_pages):
            break
        if around_pages[i] not in pages:
            pages.append(page)

    for i, page in enumerate(right_boundary):
        if i == 0 and right_boundary[i] < total_pages:
            pages.append(page)
            continue
        if (right_boundary[i] > total_pages):
            break
        if right_boundary[i] not in pages:
            pages.append(page)

    pages.sort()

    for i, page in enumerate(pages):
        if (pages[i] - pages[i - 1]) > 1:
            pagination.append("...")
        if (pages[i] > total_pages):
            break
        if pages[i] not in pagination:
            pagination.append(page)

    return ' '.join(str(e) for e in pagination)
