export default function uploadPhoto(filename) {
  const err = new Error(`${filename} cannot be processed`);
  const p = new Promise((reject) => { reject(err); });
  p.catch();
  return p;
}
