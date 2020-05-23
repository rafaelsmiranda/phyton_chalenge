def pagination(current_page=1, total_pages=10, boundaries=1, around=0):
    if total_pages < 0:
        return "Total pages should be greater than 0"

    if current_page < 0:
        return "Current page should be greater than 0"

    if current_page > total_pages:
        return "Current page exceeds total number of pages"

    left_boundary = [1]
    around_pages = [1]
    right_boundary = [1]

    for i in range(1, boundaries + 1):
        if i > 0 and i < total_pages:
            left_boundary.append(i)

    for i in range(current_page - around, current_page + around + 1):
        if i > 0 and i > left_boundary[-1] and i < total_pages:
            around_pages.append(i)

    for i in range(total_pages - boundaries + 1, total_pages):
        if i > 0 and i > around_pages[-1] and i < total_pages:
            right_boundary.append(i)

    right_boundary.append(total_pages)

    page_range = left_boundary
    for i, page in enumerate(around_pages):
        page_range.append(page)

    for i, page in enumerate(right_boundary):
        page_range.append(page)

    page_range.sort()

    footer_pagination = []
    for i, page in enumerate(page_range):
        if (page_range[i] - page_range[i - 1]) > 1:
            footer_pagination.append("...")
        if page_range[i] not in footer_pagination:
            footer_pagination.append(page)

    return ' '.join(str(e) for e in footer_pagination)
