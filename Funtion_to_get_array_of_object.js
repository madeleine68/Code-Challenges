// Create a script to accept a table name and return a list records displays
// values. 

// @param tableName - name of table to query
// @return arry - list of record display
// @return array of objects.
 //  {
 //	   "display_value" : <display value>,
 //	   "sys_id" : <sys_id>
 //  }

function listRecords(tableName, limit) {
	var answer = [];
	var recGr = new GlideRecord(tableName);

	if (limit && limit > 0 ){
		recGr.setLimit(limit);
	}

	recGr.query();

	while (recGr.next()) {
		var obj ={};
                obj.display_value = recGr.getDisplayValue();
                obj.sys_id = recGr.getUniqueValue()

		answer.push(obj);	
		
	}
	return answer
}
var list = listRecords("incident", 10)
gs.info(JSON.stringify(list,null, 4));
