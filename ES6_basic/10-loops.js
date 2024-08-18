export default function appendToEachArrayValue(array, appendString) {
  for (const idx of array) {
    const newarray = [...array];
    const value = newarray[idx];
    newarray[idx] = appendString + value;
  }

  return array;
}
