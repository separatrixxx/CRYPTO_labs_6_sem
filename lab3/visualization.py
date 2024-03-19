import numpy as np
import matplotlib.pyplot as plt


def visualization(ans, n_values):
    num_categories = len(ans)
    category_positions = np.arange(len(n_values))
    width = 0.15

    plt.figure(figsize=(12, 6))

    shift = np.linspace(-width * 2, width * 2, num_categories)

    for idx, (_, data) in enumerate(ans.items()):
        percentages = [item for item in data[1:]]
        plt.bar(category_positions + shift[idx], percentages, width=width, label=data[0])

    plt.xticks(category_positions, [str(n) for n in n_values])
    plt.xlabel('Количество символов')
    plt.ylabel('Процент совпадений')

    plt.legend(title='Типы текста', loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=3)

    plt.title('Сравнение процентов совпадений у различных типов текста')
    plt.tight_layout()
    plt.show()
