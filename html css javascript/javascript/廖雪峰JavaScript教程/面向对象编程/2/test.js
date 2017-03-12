function Student(props) {
	this.name = props.name;
	this.hello = function () {
		return this.name;
	}
}

function PrimaryStudent(props) {
	Student.call(this, props);
	this.grade    = props.grade || 1;
	this.getGrade = function () {
		return this.grade;
	}
}

PrimaryStudent.prototype.__proto__ = Student.prototype

// xiaoming ---> PrimaryStudent.prototype ---> Student.prototype ---> Object.prototype ---> null
var xiaoming = new PrimaryStudent({name:'小明',grade:2});

console.log(xiaoming.name);
console.log(xiaoming.grade);
console.log(xiaoming.hello());
console.log(xiaoming.getGrade());
console.log(xiaoming.__proto__ == PrimaryStudent.prototype);
console.log(xiaoming.__proto__.__proto__ === Student.prototype);
console.log(PrimaryStudent.prototype.constructor === PrimaryStudent);
console.log(Student.prototype.constructor === Student);
console.log(xiaoming instanceof PrimaryStudent);
console.log(xiaoming instanceof Student);