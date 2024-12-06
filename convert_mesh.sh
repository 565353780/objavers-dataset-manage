if [ "$(uname)" == "Darwin" ]; then
  PROCESSOR_NUM=$(sysctl -n hw.physicalcpu)
elif [ "$(uname)" = "Linux" ]; then
  PROCESSOR_NUM=$(cat /proc/cpuinfo | grep "processor" | wc -l)
fi

PROCESSOR_NUM=4

for i in $(seq 1 ${PROCESSOR_NUM}); do
  python convert_mesh.py &
  sleep 1
  echo "started Convertor No."$i
done

wait

echo "all Convertors started!"
