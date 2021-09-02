class LinkedList {
  constructor() {
    this.head = null;
    this.length = 0;
  }
  insertAtHead(data) {
    const newnode = new LinkedListNode(data, this.head);
    this.head = newnode;
    this.length++;
  }

  getbyindex(index) {
    if (index < 0 || index > this.length) return null;
    let current = this.head;
    for (let i = 0; i < index; i++) {
      current = current.next;
    }
    return current;
  }

  insertByIndex(index, value) {
    if (index == 0) return this.insertAtHead(value);

    const prev = this.getbyindex(index - 1);
    prev.next = new LinkedListNode(value, prev.next);
    this.length++;
  }

  removeHead() {
    this.head = this.head.next;
    this.length--;
  }
  removeByIndex(index, value) {
    if (index == 0) return this.insertAtHead();

    const prev = this.getbyindex(index - 1);
    prev.next = prev.next.next;
    this.length++;
  }

  reverse() {
    let next = null;
    let prev = null;
    let current = this.head;

    while (current !== null) {
      next = current.next;
      current.next = prev;
      prev = current;
      current = next;
    }
    this.head = prev;
  }

  print() {
    let output = "";
    let current = this.head;

    while (current) {
      output = `${output}${current.value} -> `;
      current = current.next;
    }
    console.log(`${output}null`);
  }
}

class LinkedListNode {
  constructor(value, next) {
    this.value = value;
    this.next = next;
  }
}

LinkedList.fromvalues = function (...value) {
  const ll = new LinkedList();

  for (let i = value.length - 1; i >= 0; i--) {
    ll.insertAtHead(value[i]);
  }
  return ll;
};

module.exports = LinkedList;
