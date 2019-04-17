from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, 'index.html')


def count(request):
    user_text = request.GET['text']
    total_count = len(request.GET['text'])

    word_dict = {}

    for word in user_text:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    sorted_dict = sorted(word_dict.items(), key=lambda w: w[1], reverse=True)

    return render(request, 'count.html', {'count': total_count, 'text': user_text,
                  'word_list': word_dict, 'sorted': sorted_dict})





