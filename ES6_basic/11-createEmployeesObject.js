export default function createEmployeesObject(departmentName, employees) {
  const objname = {
    [departmentName]: [...employees],
  };
  return (objname);
}
