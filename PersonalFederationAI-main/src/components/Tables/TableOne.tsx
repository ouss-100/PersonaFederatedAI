import Image from "next/image";

const TableOne = ({fiveUsers}: {fiveUsers: any[]}) => {
  return (
    <div className="rounded-sm border border-stroke bg-white px-5 pb-2.5 pt-6 shadow-default dark:border-strokedark dark:bg-boxdark sm:px-7.5 xl:pb-1">
      <h4 className="mb-6 text-xl font-semibold text-black dark:text-white">
        Latest 5 Users
      </h4>

      <div className="flex flex-col">
        <div className="grid grid-cols-3 rounded-sm bg-gray-2 dark:bg-meta-4">
          <div className="p-2.5 xl:p-5 sm:ml-32 ml-12">
            <h5 className="text-sm font-medium uppercase xsm:text-base">
              id
            </h5>
          </div>
          <div className="p-2.5 text-center xl:p-5">
            <h5 className="text-sm font-medium uppercase xsm:text-base">
              personality
            </h5>
          </div>
          <div className="block p-2.5 text-center xl:p-5">
            <h5 className="text-sm font-medium uppercase xsm:text-base">
              analysed at
            </h5>
          </div>
        </div>
        {fiveUsers.map((brand, key) => (
          <div
            className={`grid grid-cols-3 ${
              key === fiveUsers.length - 1
                ? ""
                : "border-b border-stroke dark:border-strokedark"
            }`}
            key={key}
          >
            <div className="flex items-center justify-center p-2.5 xl:p-5">
              <p className="text-black dark:text-white">{brand.id.toString().substring(0, 15)}</p>
            </div>

            <div className="flex items-center justify-center p-2.5 xl:p-5">
              <p className="text-meta-3">{brand.dominantpersonality}</p>
            </div>

            <div className="flex items-center justify-center p-2.5 xl:p-5">
              <p className="text-black dark:text-white">{brand.createdAt.toLocaleDateString('en-GB').split('/').join('-')}</p>
            </div>

          </div>
        ))}
      </div>
    </div>
  );
};

export default TableOne;
