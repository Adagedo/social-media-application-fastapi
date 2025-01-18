/*

function fib(n) {
	let table = Array(n + 1).fill(0);
	table[1] = 1;
	for (let i = 0; i <= n; i++) {
		if (i <= n) {
			table[i + 1] += table[i];
			table[i + 2] += table[i];
		}
	}

	return table[n];
}

console.log(fib(7));

function grid(m, n) {
	let table = Array(m + 1)
		.fill()
		.map(() => Array(n + 1).fill(0));
	table[1][1] = 1;
	for (let i = 0; i <= m; i++) {
		for (let j = 0; j <= n; j++) {
			const current = table[i][j];
			if (i + 1 <= m) table[i + 1][j] += current;
			if (j + 1 <= n) table[i][j + 1] += current;
		}
	}
	return table[m][n];
}
console.log(grid(3, 3));
class Nodes {
	constructor(values) {
		this.values = values;
		this.left = null;
		this.right = null;
	}
}

let a = new Nodes("a");
let b = new Nodes("b");
let c = new Nodes("c");
let d = new Nodes("d");
let e = new Nodes("e");
let f = new Nodes("f");

a.left = b;
a.right = c;
b.left = d;
b.right = e;
c.right = f;

function Breath(root) {
	if (root === null) return [];

	let result = [];
	let queue = [root];
	while (queue.length > 0) {
		let level = [];
		for (let index = 0; index < queue.length; index++) {
			let current = queue.shift();
			level.push(current.values);
			if (current.left) queue.push(current.left);
			if (current.right) queue.push(current.right);
		}
		result.push(level);
	}
	return result;
}

const me = Breath(a);
console.log(me);
function size(root) {
	if (root === null) return 0;
	return 1 + size(root.left) + size(root.right);
}

console.log(size(a));

function height(root) {
	if (root === null) return [];
	return [root.values, ...height(root.left), ...height(root.right)];
}

console.log(height(a));

const solve = (arr) => {
	let flips = 0;

	for (const element of object) {
		if (flips % 2 == 0) {
			b = b;
		} else b = !b;

		if (b % 2 == 1) continue;
		else flips += 1;
	}
	return flips;
};

class Nodes {
	constructor(node) {
		this.node = node;
		this.next_node = null;
	}
}

class LinkedList {
	constructor() {
		this.head = null;
	}

	add(node) {
		let new_nodes = new Nodes(node);
		new_nodes.next_node = this.head;
		this.head = new_nodes;
	}

	Size() {
		let count = 0;
		let current = this.head;
		while (current != null) {
			count += 1;
			current = current.new_node;
		}
		return count;
	}
}

class Min_Heap {
	constructor() {
		this.heap = [];
	}
	insert(key, value) {
		this.heap.push((key, value));
		// sift
	}
	peak() {
		if (this.heap == null) {
			return null;
		}
		return this.heap[0];
	}

	PopHeaos() {
		if (this.heap === null) {
			return null;
		}
		let min = this.heap[0];
		let last = this.heap.pop();

		if (this.heap) {
			min = last;
			this.sift_down(0);
		}
		return min;
	}

	heapify(element) {
		this.heap = element;
		const arr_re = this.heap.reverse();
		for (let index = 0; index < arr_re.length; index++) {
			this.sift_down(index);
		}
	}
	_parent(index) {
		const parent = index - 1; //2
		if (parent != 0) return parent;
	}
	_left(index) {
		const left = index * 2 + 1;
		if (left < this.heap.length) return left;
	}
	_right() {
		const right = index * 2 + 2;
		if (right < this.heap.length) return right;
	}
	sift_Up(index) {
		let parent_index = this._parent(index);
		while (
			parent_index != null &&
			this.heap[index][0] < this.heap[parent_index][0]
		) {
			this.heap[index],
				(this.heap[parent_index] = this.heap[parent_index]),
				this.heap[index];
			index = parent_index;
			parent_index = this._parent(index);
		}
	}
	sift_down(index) {
		let smallet = index;
		let left_child_index = this._left(index);
		let right_child_index = this._right(index);

		while (true) {
			if (this.heap[left_child_index] < this.heap[smallet]) {
				smallet = left_child_index;
			}
			if (this.heap[right_child_index] < this.heap[smallet]) {
				smallet = right_child_index;
			}
			if (this.heap[index] === this.heap[smallet]) break;
			this.heap[index],
				(this.heap[smallet] = this.heap[smallet]),
				this.heap[index];
			index = smallet;
		}
	}
}

//higher order functions



setTimeout(() => {
	console.log("this is a call back");
}, 1000);

let rabbit = {};
rabbit.speak = function (line) {
	console.log(`this rabbit says ${line}`);
};

// prototypes

let empty = {};
console.log(empty.toString);
console.log(empty.toString());
function Rabbit(type) {
	this.type = type;
}

Rabbit.prototype.speak = function () {
	console.log(`the rabbit says ${this.type}`);
};

let wierdRabbit = new Rabbit("wierd");
console.log(wierdRabbit);
console.log(wierdRabbit.speak());
console.log(wierdRabbit.type);

class Rats {
	constructor(type) {
		this.type = type;
	}
	speak(line) {
		return `the ${this.type} says ${line}`;
	}
}

let rats = new Rats("wild");
console.log(rats.speak("wierd"));
console.log(rats.type);
let killerRabbits = new Rats("killers");

Rats.prototype.teeth = "small";
console.log(killerRabbits.teeth);

class InputError extends Error {}

const params = async (params) => {
	return params();
};

let five = Promise.resolve("name");

function storage(nest, name) {
	return new Promise((resolve) => {
		nest.readStorage(name, (result) => resolve(result));
	});
}

const keyPadObjects = {
	2: "abc",
	3: "def",
	4: "ghi",
	5: "jik",
	6: "mno",
	7: "pqrs",
	8: "tvs",
	9: "wxyz",
};

const Count = (array) => {
	if (arr.length <= 1) return arr;
	const Graphs = {};

	const helper = (arr, target) => {
		if (arr.length <= 1) return arr;
		let count = 0;

		for (let index = 0; index < array.length; index++) {
			if (array[index] === target) {
				count++;
			}
		}

		return target, count;
	};
	for (let index = 0; index < array.length; index++) {
		let target,
			count = helper(array, array[index]);
		console.log(target, count);
		Graphs[target] = count;
	}

	return Graphs;
};

let arr = ["me", "uo", "me", "me", "me"];

const helper = (array, target) => {
	if (array.length <= 1) return array;
	let count = 0;

	for (let index = 0; index < array.length; index++) {
		if (array[index] === target) {
			count++;
		}
	}

	return { target: target, count: count };
};

console.log(helper(arr, "me"));
*/

const fib = (n) => {
	const Table = Array(n + 1).fill(0);
	Table[1] = 1;

	for (let index = 0; index <= n; index++) {
		Table[index + 1] += Table[index];
		Table[index + 2] += Table[index];
	}

	return Table[n];
};
console.log(fib(6));

const Grid = (m, n) => {
	const table = Array(m + 1)
		.fill()
		.map(() => Array(n + 1).fill(0));
	table[1][1] = 1;

	for (let i = 0; i <= m; i++) {
		for (let j = 0; j <= n; j++) {
			const current = table[i][j];
			if (j + 1 <= n) table[i][j + 1] += current;
			if (i + 1 <= m) table[i + 1][j] += current;
		}
	}
	return table[m][n];
};
console.log(Grid(3, 3));

const canSum = (arr, target) => {
	const table = Array(target + 1).fill(false);
	table[0] = true;

	for (let i = 0; i <= target; i++) {
		if (table[i] === true) {
			for (let num of arr) {
				table[i + num] = true;
			}
		}
	}
	return table[target];
};

console.log(canSum([1, 2, 3, 4, 5], 7));
console.log(canSum([4, 5, 6, 7], 3));
console.log(canSum([16, 5, 4, 8], 7));

function calculate(string) {
	let result;
	return result;
}
