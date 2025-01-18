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
function Solve(number, stringArr) {
	const result = [];
	const Combinations = (number) => {
		const strings_nums = String(number);
		const result = [];

		const dfs = (i, path) => {
			if (i === strings_nums.length) {
				result.push(path.join(""));
				return;
			}

			for (let char of keyPadObjects[strings_nums[i]]) {
				path.push(char);
				dfs(i + 1, path);
				path.pop();
			}
		};
		dfs(0, []);
		return result;
	};
	const LongestSubString = (
		string1,
		string2,
		idx1 = 0,
		idx2 = 0,
		memo = {}
	) => {
		const indexs = idx1 + "," + idx2;
		if (indexs in memo) return memo[indexs];
		if (idx1 === string1.length || idx2 === string2.length) return 0;
		if (string1[idx1] === string2[idx2]) {
			memo[indexs] = LongestSubString(
				string1,
				string2,
				idx1 + 1,
				idx2 + 1,
				memo
			);
			return 1 + memo[indexs];
		} else {
			const option1 = LongestSubString(string1, string2, idx1 + 1, idx2, memo);
			const option2 = LongestSubString(
				string1,
				string2,
				idx1,
				idx2 + 1,
				memo
			);
			memo[indexs] = Math.max(option1, option2);
			return memo[indexs];
		}
	};

	const Count = (array) => {
		if (array.length <= 1) return array;
		const Graphs = {};

		const helper = (array, target) => {
			if (array.length <= 1) return array;
			let count = 0;

			for (let items of array) {
				if (items === target) {
					count += 1;
				}
			}

			return { target: target, count: count };
		};
		for (let index = 0; index < array.length; index++) {
			const { target, count } = helper(array, array[index]);
			Graphs[target] = count;
		}

		return Graphs;
	};
	const string_num_combination = Combinations(number);

	for (let i = 0; i < string_num_combination.length; i++) {
		for (let j = 0; j < stringArr.length; j++) {
			const subs = LongestSubString(string_num_combination[i], stringArr[j]);
			if (stringArr[j].length === subs) {
				result.push(stringArr[j]);
			}
		}
	}

	const the_result = Count(result);
	const finalResult = Object.keys(the_result);
	return finalResult;
}

const string_values = [
	"foo",
	"bar",
	"baz",
	"foobar",
	"emo",
	"cap",
	"car",
	"cat",
];
const someNums = 3662277;
const response = Solve(someNums, string_values);
console.log(response);
