Columns in csv file
id,name,nameHindi,parentId

id: unique id for each name
name: Name of the person
nameHindi: Name of the person in Hindi
parentId: used to link children to parent (Relation with id field)

Expected Output Structure
{
  id: string;
  name: string;        // English name of the family member
  nameHindi?: string;  // Hindi name of the family member (optional)
  children: {
    childId: string;
    childList: FamilyTree[];
  };
}

childId is auto generated, it is id + "-Kids"
