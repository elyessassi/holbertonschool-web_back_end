export default function appendToEachArrayValue(array, appendString) {
  for (const idx of array) {
    let array;
    const value = array[idx];
    array[idx] = appendString + value;
  }

  return array;
}
