def pagination(current_page=1, total_pages=10, boundaries=1, around=0):
    left_boundary = []
    right_boundary = []
    around_pages = []

    if current_page > total_pages:
        return "Current page exceeds total number of pages"

    for i in range(1, boundaries + 1):
        left_boundary.append(i)

    for i in range(current_page - around, current_page + around + 1):
        around_pages.append(i)

    for i in range(total_pages - boundaries, total_pages):
        right_boundary.append(i+1)

    left_boundary = [x for x in left_boundary if x not in around_pages]
    around_pages = [x for x in around_pages if x not in right_boundary]

    pages = left_boundary + around_pages + right_boundary
    pagination = []
    for i, page in enumerate(pages):
        if i == 0:
            pagination.append(str(page))
            continue
        if (pages[i] - pages[i - 1]) > 1:
            pagination.append("...")

        pagination.append(str(page))

    return ' '.join(str(e) for e in pagination)
