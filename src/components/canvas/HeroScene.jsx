import { Suspense, useRef, useMemo } from "react";
import { Canvas, useFrame } from "@react-three/fiber";
import { OrbitControls, Preload, Float, useTexture } from "@react-three/drei";
import * as THREE from "three";
import Loader from "../Loader";


/* Procedural Neural Network / AI Brain Visualization */
const NeuralNetwork = () => {
  const groupRef = useRef();
  const nodesRef = useRef();

  // Generate node positions
  const nodePositions = useMemo(() => {
    const positions = [];
    for (let i = 0; i < 200; i++) {
      positions.push([
        (Math.random() - 0.5) * 16,
        (Math.random() - 0.5) * 12,
        (Math.random() - 0.5) * 12,
      ]);
    }
    return positions;
  }, []);

  // Generate connection lines
  const lineGeometries = useMemo(() => {
    const geos = [];
    for (let i = 0; i < nodePositions.length; i++) {
      for (let j = i + 1; j < nodePositions.length; j++) {
        const dist = Math.sqrt(
          Math.pow(nodePositions[i][0] - nodePositions[j][0], 2) +
          Math.pow(nodePositions[i][1] - nodePositions[j][1], 2) +
          Math.pow(nodePositions[i][2] - nodePositions[j][2], 2)
        );
        if (dist < 2.5) {
          const points = [
            new THREE.Vector3(...nodePositions[i]),
            new THREE.Vector3(...nodePositions[j]),
          ];
          const geo = new THREE.BufferGeometry().setFromPoints(points);
          geos.push(geo);
        }
      }
    }
    return geos;
  }, [nodePositions]);

  useFrame((state) => {
    if (groupRef.current) {
      groupRef.current.rotation.y = state.clock.getElapsedTime() * 0.02;
      groupRef.current.rotation.x = Math.sin(state.clock.getElapsedTime() * 0.02) * 0.05;
    }
  });

  return (
    <group ref={groupRef}>
      {/* Nodes */}
      {nodePositions.map((pos, i) => (
        <mesh key={i} position={pos}>
          <sphereGeometry args={[0.05, 16, 16]} />
          <meshStandardMaterial
            color={i % 2 === 0 ? "#00e5ff" : "#9d4edd"}
            emissive={i % 2 === 0 ? "#00e5ff" : "#9d4edd"}
            emissiveIntensity={0.8}
          />
        </mesh>
      ))}
      {/* Connections */}
      {lineGeometries.map((geo, i) => (
        <line key={`line-${i}`} geometry={geo}>
          <lineBasicMaterial
            color="#00e5ff"
            transparent
            opacity={0.12}
          />
        </line>
      ))}

    </group>
  );
};

const HeroCanvas = () => {
  return (
    <Canvas
      frameloop="always"
      shadows
      dpr={[1, 2]}
      camera={{ position: [0, 0, 5], fov: 45 }}
      gl={{ preserveDrawingBuffer: true }}
    >
      <Suspense fallback={<Loader />}>
        <OrbitControls
          enableZoom={false}
          maxPolarAngle={Math.PI}
          minPolarAngle={0}
          autoRotate
          autoRotateSpeed={0.3}
        />
        <ambientLight intensity={0.4} />
        <pointLight position={[10, 10, 10]} intensity={1.5} color="#00e5ff" />
        <pointLight position={[-10, -10, -10]} intensity={1} color="#9d4edd" />
        <NeuralNetwork />
      </Suspense>
      <Preload all />
    </Canvas>
  );
};

export default HeroCanvas;
