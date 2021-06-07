// Create a script to accept a table name and return a list records displays
// values. 

// @param tableName - name of table to query
// @return arry - list of record display

function listRecords(tableName) {
	var answer = [];
	var recGr = new GlideRecord(tableName);
	recGr.query();

	while (recGr.next()) {
		answer.push(recGr.getDisplayValue());
	}
	return answer
}

gs.info(listRecords("incident").join(','));
