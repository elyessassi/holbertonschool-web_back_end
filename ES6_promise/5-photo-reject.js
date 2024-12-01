export default function uploadPhoto(filename) {
  const err = new Error(`${filename} cannot be processed`);
  const p = Promise.reject(err).catch();
  return p;
}
