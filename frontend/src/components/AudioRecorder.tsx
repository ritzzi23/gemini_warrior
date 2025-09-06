import React from 'react';
import { useAudioRecorder, type RecordingSource } from '../hooks/useAudioRecorder';

interface AudioRecorderProps {
  onRecordingComplete: (audioBlob: Blob) => void;
  recordingSource: RecordingSource;
  setRecordingSource: (source: RecordingSource) => void;
  onClose: () => void;
}

const AudioRecorder: React.FC<AudioRecorderProps> = ({ onRecordingComplete, recordingSource, setRecordingSource, onClose }) => {
  const {
    isRecording,
    setIsRecording,
    recordingTime,
    audioLevel,
    startRecording,
    stopRecording,
  } = useAudioRecorder({ recordingSource, onRecordingComplete });

  const formatTime = (seconds: number) => {
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
  };

  return (
    <>
      {/* Blur overlay for entire page */}
      <div className="fixed inset-0 bg-black/20 backdrop-blur-md z-40 animate-fade-in"></div>
      {/* Responsive Modal */}
      <div className="fixed z-50 w-full sm:w-auto left-1/2 top-1/2 sm:left-[25%] sm:top-1/2 transform -translate-x-1/2 -translate-y-1/2 sm:-translate-y-1/2 sm:bottom-auto">
        <div className="bg-theme-modal rounded-t-2xl sm:rounded-2xl shadow-2xl border border-theme-modal p-3 sm:p-6 w-full sm:min-w-[340px] max-w-md mx-auto relative">
          {/* Close Button */}
          <button
            onClick={onClose}
            className="absolute top-2 right-2 sm:top-4 sm:right-4 p-2 rounded-lg bg-secondary-100 dark:bg-secondary-900 hover:bg-secondary-200 dark:hover:bg-secondary-800 transition-colors duration-200 text-theme-secondary dark:text-secondary-100 hover:text-theme-primary dark:hover:text-white"
            aria-label="Close recording modal"
          >
            <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
          <div className="flex items-center justify-between mb-2 sm:mb-4">
            <div className="flex items-center gap-2 sm:gap-3">
              <div className={`w-3 h-3 rounded-full ${isRecording ? 'bg-danger-500 animate-pulse' : 'bg-secondary-400'}`}></div>
              <span className="font-semibold text-xs sm:text-base text-theme-primary">
                {isRecording ? 'Recording...' : 'Ready to Record'}
              </span>
            </div>
            {isRecording && (
              <div className="text-sm font-mono text-theme-secondary">
                {formatTime(recordingTime)}
              </div>
            )}
          </div>

          {/* Source Selection */}
          <div className="flex justify-center gap-2 sm:gap-4 mb-2 sm:mb-4">
            <button
              className={`flex items-center gap-1 sm:gap-2 px-2 sm:px-4 py-2 rounded-lg border text-xs sm:text-sm font-medium transition-all duration-150
                ${recordingSource === 'mic' ? 'bg-primary-100 border-primary-400 text-primary-700' : 'bg-secondary-100 border-secondary-300 text-secondary-500'}
              `}
              onClick={() => setRecordingSource('mic')}
              disabled={isRecording}
            >
              <svg className="w-4 h-4 sm:w-5 sm:h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 1v22m6-6a6 6 0 01-12 0" /></svg>
              Microphone
            </button>
            <button
              className={`flex items-center gap-1 sm:gap-2 px-2 sm:px-4 py-2 rounded-lg border text-xs sm:text-sm font-medium transition-all duration-150
                ${recordingSource === 'system' ? 'bg-primary-100 border-primary-400 text-primary-700' : 'bg-secondary-100 border-secondary-300 text-secondary-500'}
                `}
              onClick={() => setRecordingSource('system')}
              disabled={isRecording}
            >
              <svg className="w-4 h-4 sm:w-5 sm:h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 4h18M3 10h18M3 16h18" /></svg>
              System Audio
            </button>
          </div>

          {/* Audio Level Visualization */}
          {isRecording && (
            <div className="mb-2 sm:mb-4">
              <div className="flex items-center justify-center gap-0.5 sm:gap-1 h-6 sm:h-8">
                {Array.from({ length: 20 }, (_, i) => (
                  <div
                    key={i}
                    className="w-1 bg-secondary-300 rounded-full transition-all duration-75"
                    style={{
                      height: `${Math.max(4, (audioLevel / 255) * 32 * Math.random())}px`,
                      backgroundColor: audioLevel > 100 ? 'var(--danger-500)' : 'var(--primary-500)'
                    }}
                  />
                ))}
              </div>
            </div>
          )}

          {/* Recording Instructions */}
          <div className="text-center mb-2 sm:mb-4">
            <p className="text-xs sm:text-sm text-theme-secondary">
              {isRecording 
                ? 'Speak clearly into your microphone' 
                : 'Click the button below to start recording'
              }
            </p>
          </div>

          {/* Control Button */}
          <div className="flex justify-center">
            <button
              onClick={() => setIsRecording(!isRecording)}
              className={`relative group transition-all duration-300 ${
                isRecording 
                  ? 'bg-danger-500 hover:bg-danger-600 scale-110' 
                  : 'bg-primary-500 hover:bg-primary-600 hover:scale-105'
              } text-white rounded-full p-3 sm:p-4 shadow-lg hover:shadow-xl`}
              style={{ minWidth: 44, minHeight: 44 }}
              aria-label={isRecording ? 'Stop recording' : 'Start recording'}
            >
              {isRecording ? (
                <svg className="w-6 h-6 sm:w-7 sm:h-7" fill="currentColor" viewBox="0 0 24 24">
                  <rect x="7" y="7" width="10" height="10" rx="2" />
                </svg>
              ) : (
                <svg className="w-6 h-6 sm:w-7 sm:h-7" fill="none" stroke="currentColor" strokeWidth="2" viewBox="0 0 24 24">
                  <path d="M12 1a3 3 0 013 3v6a3 3 0 11-6 0V4a3 3 0 013-3zm5 10a5 5 0 01-10 0m10 0v2a7 7 0 01-14 0v-2m14 0h2m-2 0h-2m-6 0H4m2 0h2" />
                </svg>
              )}
              <div className={`absolute inset-0 rounded-full ${
              isRecording 
                ? 'bg-danger-400 animate-ping opacity-75' 
                : 'bg-primary-400 opacity-0 group-hover:opacity-50 transition-opacity'
              }`}></div>
            </button>
          </div>

          {/* Status Text */}
          <div className="text-center mt-4">
            <p className="text-xs text-theme-muted">
              {isRecording 
                ? 'Click to stop recording' 
                : 'Your voice will be transcribed automatically'
              }
            </p>
          </div>
        </div>
      </div>
    </>
  );
};

export default AudioRecorder;
