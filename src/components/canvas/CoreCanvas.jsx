import { Suspense, useRef } from "react";
import { Canvas, useFrame } from "@react-three/fiber";
import { OrbitControls, Preload, Float, MeshDistortMaterial } from "@react-three/drei";
import Loader from "../Loader";

const AbstractCore = () => {
  const groupRef = useRef();

  useFrame((state) => {
    if (groupRef.current) {
      groupRef.current.rotation.y = state.clock.getElapsedTime() * 0.2;
      groupRef.current.rotation.x = state.clock.getElapsedTime() * 0.1;
    }
  });

  return (
    <group ref={groupRef}>
      <Float speed={2} rotationIntensity={1} floatIntensity={2}>
        <mesh>
          <icosahedronGeometry args={[1, 0]} />
          <meshStandardMaterial
            color="#00e5ff"
            wireframe
            emissive="#00e5ff"
            emissiveIntensity={0.5}
          />
        </mesh>
        <mesh scale={0.6}>
          <octahedronGeometry args={[1, 0]} />
          <meshStandardMaterial
            color="#9d4edd"
            emissive="#9d4edd"
            emissiveIntensity={1}
          />
        </mesh>
        <mesh scale={1.2}>
          <sphereGeometry args={[1, 32, 32]} />
          <MeshDistortMaterial
            color="#151030"
            transparent
            opacity={0.6}
            distort={0.4}
            speed={2}
            envMapIntensity={1}
            clearcoat={1}
            clearcoatRoughness={0.1}
          />
        </mesh>
      </Float>
    </group>
  );
};

const CoreCanvas = () => {
  return (
    <Canvas
      frameloop="always"
      shadows
      camera={{ position: [0, 0, 4.5], fov: 45 }}
      gl={{ preserveDrawingBuffer: true }}
    >
      <Suspense fallback={<Loader />}>
        <OrbitControls
          enableZoom={false}
          maxPolarAngle={Math.PI / 2}
          minPolarAngle={Math.PI / 2}
          autoRotate
          autoRotateSpeed={1}
        />
        <ambientLight intensity={0.5} />
        <directionalLight position={[10, 10, 5]} intensity={1.5} color="#00e5ff" />
        <directionalLight position={[-10, -10, -5]} intensity={1} color="#9d4edd" />
        <AbstractCore />
      </Suspense>
      <Preload all />
    </Canvas>
  );
};

export default CoreCanvas;
