// Create a script to accept a table name and return a list records displays
// values. 

// @param tableName - name of table to query
// @return arry - list of record display

function listRecords(tableName, limit) {
	var answer = [];
	var recGr = new GlideRecord(tableName);

	if (limit && limit > 0 ){
		recGr.setLimit(limit);
	}

	recGr.query();

	while (recGr.next()) {
		answer.push(recGr.getDisplayValue());
	}
	return answer
}

gs.info(listRecords("incident", 10).join('\n'));
