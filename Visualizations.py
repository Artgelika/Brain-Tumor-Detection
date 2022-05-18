import matplotlib.pyplot as plt


def printed_data(X_set, y_set):
    print("X_train:", len(X_set))
    print("y_train:", len(y_set))

    print(X_set[:5], X_set[500:505], X_set[-5:])
    print(y_set[:5], y_set[500:505], y_set[-5:])


def visualize_photos(dataloader: list, y_label: list, class_names: list, one_size: int) -> None:
    assert one_size > 0 and type(one_size) is int
    fig = plt.figure(figsize=(10, 10))
    fig.suptitle("Examples of images from dataset")
    for i in range(one_size*one_size):
        plt.subplot(one_size, one_size, i+1)
        plt.imshow(dataloader[i], cmap=plt.cm.binary)
        plt.xticks([])
        plt.yticks([])
        plt.xlabel(class_names[int(y_label[i])])

    plt.show()
