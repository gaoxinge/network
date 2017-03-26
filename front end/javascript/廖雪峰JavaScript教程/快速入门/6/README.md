# 条件

## switch

```javascript
cvar day = new Date().getDay();

switch (day) {
	case 0:
		x = "Today is Sunday";
		break;
	case 1:
		x = "Today is Monday";
		break;
	case 2:
		x = "Today is Tuesday";
		break;
	case 3:
		x = "Today is Wednesday";
		break;
	case 4:
		x = "Today is Thursday";
		break;
	case 5:
		x = "Today is Friday";
		break;
	case 6:
		x = "Today is Saturday";
		break;
}

console.log(x);
```